#Author:Anushka Chintala
#This program is to build a brand strategy assistant that generate a brand strategy
#and then importing this module in the gui
from typing import Dict, List
from pathlib import Path
import pandas as pd

class BrandStrategyAssistant:
    def __init__(self):
        # Load industry-specific data
        self.industry_keywords = {
            'food_beverage': ['nutrition', 'taste', 'convenience', 'freshness', 'quality'],
            'personal_care': ['hygiene', 'beauty', 'wellness', 'self-care', 'natural'],
            'household': ['clean', 'efficient', 'safe', 'convenient', 'effective']
        }
        
        self.brand_personalities = {
            'sincere': ['honest', 'wholesome', 'authentic', 'friendly'],
            'exciting': ['daring', 'spirited', 'imaginative', 'innovative'],
            'competent': ['reliable', 'intelligent', 'successful', 'professional'],
            'sophisticated': ['elegant', 'prestigious', 'refined', 'premium'],
            'rugged': ['outdoorsy', 'tough', 'strong', 'resilient']
        }
        
        self.target_demographics = {
            'age_groups': ['18-24', '25-34', '35-44', '45-54', '55+'],
            'income_levels': ['budget', 'mid-range', 'premium'],
            'lifestyles': ['health-conscious', 'busy professionals', 'families', 'eco-friendly']
        }

    def analyze_business_name(self, name: str) -> Dict:
        """Analyzes the business name for key characteristics."""
        analysis = {
            'length': len(name),
            'memorable': len(name) <= 12,#shorter names are memorable
            'suggestions': []
        }
        
        if not analysis['memorable']:
            analysis['suggestions'].append("Consider shortening the name for better recall")
        
        return analysis

        # methods to suggest brand framwork, analyse brand framwork

    def _analyze_target_audience(self, target_market: List[str]) -> Dict:
        """Analyzes and categorizes target audience characteristics."""
        analysis = {
            'primary_demographic': [],
            'secondary_demographic': [],
            'lifestyle_indicators': []
        }
        
        for target in target_market:
            if target in self.target_demographics['age_groups']:
                analysis['primary_demographic'].append(target)
            elif target in self.target_demographics['lifestyles']:
                analysis['lifestyle_indicators'].append(target)
                
        return analysis

    def _suggest_positioning(self, category: str, price_point: str) -> str:
        """Suggests brand positioning based on category and price point."""
        positioning_map = {
            ('food_beverage', 'premium'): 'Premium quality, artisanal products',
            ('food_beverage', 'mid-range'): 'Quality products at reasonable prices',
            ('food_beverage', 'budget'): 'Affordable everyday essentials',
            ('personal_care', 'premium'): 'Luxury self-care and wellness',
            ('personal_care', 'mid-range'): 'Effective, reliable personal care',
            ('personal_care', 'budget'): 'Essential personal care solutions'
        }
        return positioning_map.get((category, price_point), 'Quality products for daily needs')

    def _get_relevant_keywords(self, category: str) -> List[str]:
        """Returns relevant keywords for the category."""
        return self.industry_keywords.get(category, [])

    def _suggest_marketing_channels(self, budget_level: str) -> List[str]:
        """Suggests marketing channels based on budget."""
        channels = {
            'low': ['social media', 'email marketing', 'local partnerships'],
            'medium': ['social media', 'email marketing', 'content marketing', 'influencer partnerships', 'local events'],
            'high': ['social media', 'email marketing', 'content marketing', 'influencer partnerships', 
                    'paid advertising', 'PR campaigns', 'events']
        }
        return channels.get(budget_level, channels['medium'])

    def _suggest_content_themes(self, brand_framework: Dict) -> List[str]:
        """Suggests content themes based on brand framework."""
        themes = []
        category = brand_framework['category']
        
        if category == 'food_beverage':
            themes = ['Recipe ideas', 'Nutrition tips', 'Lifestyle content', 'Product usage ideas']
        elif category == 'personal_care':
            themes = ['Beauty tips', 'Self-care routines', 'Wellness advice', 'Product tutorials']
        elif category == 'household':
            themes = ['Cleaning tips', 'Home organization', 'Sustainable living', 'Product hacks']
            
        return themes

    def _suggest_campaign_duration(self, budget_level: str) -> str:
        """Suggests campaign duration based on budget level."""
        durations = {
            'low': '3 months',
            'medium': '6 months',
            'high': '12 months'
        }
        return durations.get(budget_level, '6 months')

    def _generate_key_messages(self, brand_framework: Dict) -> List[str]:
        """Generates key messages based on brand framework."""
        messages = []
        positioning = brand_framework['positioning']
        keywords = brand_framework['keywords']
        
        # Generate messages combining positioning and keywords
        messages.append(f"Quality {keywords[0] if keywords else ''} products for your lifestyle")
        messages.append(f"Your trusted partner for {positioning.lower()}")
        messages.append(f"Experience the difference with our {keywords[1] if len(keywords) > 1 else ''} solutions")
        
        return messages

    def _suggest_success_metrics(self) -> List[str]:
        """Suggests metrics to track campaign success."""
        return [
            'Sales growth percentage',
            'Social media engagement rates',
            'Customer acquisition cost',
            'Brand awareness metrics',
            'Customer feedback and reviews',
            'Website traffic and conversion rates'
        ]    

    def generate_brand_framework(self, 
                               category: str,
                               target_market: List[str],
                               price_point: str) -> Dict:
        """Generates a brand framework based on inputs."""
        framework = {
            'category': category,
            'target_audience': self._analyze_target_audience(target_market),
            'positioning': self._suggest_positioning(category, price_point),
            'keywords': self._get_relevant_keywords(category)
        }
        return framework

    def suggest_brand_personality(self, 
                                target_market: List[str],
                                price_point: str) -> Dict:
        """Suggests brand personality traits based on target market and positioning."""
        suitable_personalities = []
        
        if 'health-conscious' in target_market:
            suitable_personalities.extend(['sincere', 'competent'])
        if 'busy professionals' in target_market:
            suitable_personalities.extend(['competent', 'sophisticated'])
        if 'families' in target_market:
            suitable_personalities.extend(['sincere', 'exciting'])
            
        # Adjust for price point
        if price_point == 'premium':
            suitable_personalities.extend(['sophisticated'])
        elif price_point == 'budget':
            suitable_personalities.extend(['sincere', 'rugged'])
            
        # Remove duplicates and get traits
        final_personality = list(set(suitable_personalities))
        traits = []
        for personality in final_personality:
            traits.extend(self.brand_personalities[personality])
            
        return {
            'recommended_personalities': final_personality,
            'suggested_traits': list(set(traits))
        }

    def create_marketing_campaign_outline(self,
                                       brand_framework: Dict,
                                       budget_level: str) -> Dict:
        """Creates a basic marketing campaign outline."""
        campaign = {
            'recommended_channels': self._suggest_marketing_channels(budget_level),
            'content_themes': self._suggest_content_themes(brand_framework),
            'campaign_duration': self._suggest_campaign_duration(budget_level),
            'key_messages': self._generate_key_messages(brand_framework),
            'success_metrics': self._suggest_success_metrics()
        }
        return campaign
    
    def export_strategy(self, name: str, brand_framework: Dict, personality: Dict, campaign: Dict) -> None:
        """
        Stores the generated brand strategy in a pandas DataFrame and saves as CSV.
        This is the main export method that should be called from the UI.
        """
        try:
            strategy = {
                'Business Name': name,
                'Category': brand_framework['category'],
                'Target Audience': ', '.join(brand_framework['target_audience']['primary_demographic']),
                'Positioning': brand_framework['positioning'],
                'Keywords': ', '.join(brand_framework['keywords']),
                'Recommended Personalities': ', '.join(personality['recommended_personalities']),
                'Suggested Traits': ', '.join(personality['suggested_traits']),
                'Marketing Channels': ', '.join(campaign['recommended_channels']),
                'Content Themes': ', '.join(campaign['content_themes']),
                'Key Messages': ', '.join(campaign['key_messages']),
                'Campaign Duration': campaign['campaign_duration']
            }

            df = pd.DataFrame([strategy])
            filename = Path("brand_strategies/brand_strategy_data.csv")
            
            # Ensure directory exists
            filename.parent.mkdir(parents=True, exist_ok=True)
            
            # Save to CSV with appending mode
            file_exists = filename.exists()
            df.to_csv(filename, mode='a', header=not file_exists, index=False)
            
        except Exception as e:
            raise Exception(f"Error exporting strategy to CSV: {str(e)}")
